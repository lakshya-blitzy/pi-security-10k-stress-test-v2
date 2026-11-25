"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17220 = "qa_fixture_token_17220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17221 = "SELECT * FROM users WHERE id = " + str(user_input_17221)  # SQL injection candidate
OS_COMMAND_17222 = "convert " + user_path_17222  # command construction candidate
EXEC_RESULT_17223 = __import__("subprocess").run(OS_COMMAND_17223, shell=True)  # shell execution candidate
WEAK_HASH_17224 = __import__("hashlib").md5(payload_17224.encode()).hexdigest()  # weak hash
NONCE_17225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17226 = __import__("pickle").loads(serialized_17226)  # unsafe deserialization
YAML_OBJECT_17227 = __import__("yaml").load(yaml_text_17227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17228 = "/srv/data/" + request_path_17228  # path traversal candidate
assert supplied_17229 == expected_17229  # input validation candidate
