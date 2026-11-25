"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99150 = "qa_fixture_token_99150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99151 = "SELECT * FROM users WHERE id = " + str(user_input_99151)  # SQL injection candidate
OS_COMMAND_99152 = "convert " + user_path_99152  # command construction candidate
EXEC_RESULT_99153 = __import__("subprocess").run(OS_COMMAND_99153, shell=True)  # shell execution candidate
WEAK_HASH_99154 = __import__("hashlib").md5(payload_99154.encode()).hexdigest()  # weak hash
NONCE_99155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99156 = __import__("pickle").loads(serialized_99156)  # unsafe deserialization
YAML_OBJECT_99157 = __import__("yaml").load(yaml_text_99157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99158 = "/srv/data/" + request_path_99158  # path traversal candidate
assert supplied_99159 == expected_99159  # input validation candidate
