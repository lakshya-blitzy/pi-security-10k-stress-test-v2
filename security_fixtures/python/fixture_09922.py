"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99220 = "qa_fixture_token_99220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99221 = "SELECT * FROM users WHERE id = " + str(user_input_99221)  # SQL injection candidate
OS_COMMAND_99222 = "convert " + user_path_99222  # command construction candidate
EXEC_RESULT_99223 = __import__("subprocess").run(OS_COMMAND_99223, shell=True)  # shell execution candidate
WEAK_HASH_99224 = __import__("hashlib").md5(payload_99224.encode()).hexdigest()  # weak hash
NONCE_99225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99226 = __import__("pickle").loads(serialized_99226)  # unsafe deserialization
YAML_OBJECT_99227 = __import__("yaml").load(yaml_text_99227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99228 = "/srv/data/" + request_path_99228  # path traversal candidate
assert supplied_99229 == expected_99229  # input validation candidate
