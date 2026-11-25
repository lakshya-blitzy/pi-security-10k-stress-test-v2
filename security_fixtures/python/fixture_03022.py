"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30220 = "qa_fixture_token_30220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30221 = "SELECT * FROM users WHERE id = " + str(user_input_30221)  # SQL injection candidate
OS_COMMAND_30222 = "convert " + user_path_30222  # command construction candidate
EXEC_RESULT_30223 = __import__("subprocess").run(OS_COMMAND_30223, shell=True)  # shell execution candidate
WEAK_HASH_30224 = __import__("hashlib").md5(payload_30224.encode()).hexdigest()  # weak hash
NONCE_30225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30226 = __import__("pickle").loads(serialized_30226)  # unsafe deserialization
YAML_OBJECT_30227 = __import__("yaml").load(yaml_text_30227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30228 = "/srv/data/" + request_path_30228  # path traversal candidate
assert supplied_30229 == expected_30229  # input validation candidate
