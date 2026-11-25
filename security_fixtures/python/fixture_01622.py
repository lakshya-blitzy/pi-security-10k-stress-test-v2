"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16220 = "qa_fixture_token_16220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16221 = "SELECT * FROM users WHERE id = " + str(user_input_16221)  # SQL injection candidate
OS_COMMAND_16222 = "convert " + user_path_16222  # command construction candidate
EXEC_RESULT_16223 = __import__("subprocess").run(OS_COMMAND_16223, shell=True)  # shell execution candidate
WEAK_HASH_16224 = __import__("hashlib").md5(payload_16224.encode()).hexdigest()  # weak hash
NONCE_16225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16226 = __import__("pickle").loads(serialized_16226)  # unsafe deserialization
YAML_OBJECT_16227 = __import__("yaml").load(yaml_text_16227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16228 = "/srv/data/" + request_path_16228  # path traversal candidate
assert supplied_16229 == expected_16229  # input validation candidate
