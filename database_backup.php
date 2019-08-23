$config = [
    // ip ����� �������, � �������� ����� ���������� ����
    'ip'              => '127.0.0.1',
    // ���� �� ����� � ������� ����� ������ ����� ���
    'path'            => '/home/nastya/web/dhp/database_backups',
    // ������ ����� ����� ����� ����. ������ <date> ����������� ���� � ������� 2015-04-19
    'filenamePattern' => 'dump_<date>.sql',
    // ������������ ���������� ������, ���������� �� �������
    'maxFilesCount'   => 3,
    // ��������� ����������� � ��
    'db' => [
        'name'     => 'dhp',
        'user'     => 'SYSDBA',
        'password' => 'masterkey',
    ],
];
 
$ip = !empty($config['ip']) ? "-h $config[ip]" : '';
$filename = str_replace('<date>', '$(date +%Y-%m-%d)', $config['filenamePattern']);
$command = "mysqldump $ip -u {$config['db']['user']} -p{$config['db']['password']} --extended-insert=false {$config['db']['name']} > {$config['path']}/$filename";
 
exec($command);
 
if (!empty($config['maxFilesCount'])) {
    cleanDirectory($config['path'], $config['maxFilesCount']);
}
 
/**
 * Clears the directory of the files, leaving no more than $maxFilesCount number of files
 *
 * @param string $dir
 * @param string $maxFilesCount
 */
function cleanDirectory($dir, $maxFilesCount)
{
    $filenames = [];
 
    foreach(scandir($dir) as $file) {
        $filename = "$dir/$file";
        if (is_file($filename)) {
            $filenames[] = $filename;
        }
    }
 
    if (count($filenames) <= $maxFilesCount) {
        return;
    }
 
    $freshFilenames = array_reverse($filenames);
    array_splice($freshFilenames, $maxFilesCount);
    $oldFilenames = array_diff($filenames, $freshFilenames);
 
    foreach ($oldFilenames as $filename) {
        unlink($filename);
    }
}