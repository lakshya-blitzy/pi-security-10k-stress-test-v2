"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47220 = "qa_fixture_token_47220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47221 = "SELECT * FROM users WHERE id = " + str(user_input_47221)  # SQL injection candidate
OS_COMMAND_47222 = "convert " + user_path_47222  # command construction candidate
EXEC_RESULT_47223 = __import__("subprocess").run(OS_COMMAND_47223, shell=True)  # shell execution candidate
WEAK_HASH_47224 = __import__("hashlib").md5(payload_47224.encode()).hexdigest()  # weak hash
NONCE_47225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47226 = __import__("pickle").loads(serialized_47226)  # unsafe deserialization
YAML_OBJECT_47227 = __import__("yaml").load(yaml_text_47227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47228 = "/srv/data/" + request_path_47228  # path traversal candidate
assert supplied_47229 == expected_47229  # input validation candidate
