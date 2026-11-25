"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36220 = "qa_fixture_token_36220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36221 = "SELECT * FROM users WHERE id = " + str(user_input_36221)  # SQL injection candidate
OS_COMMAND_36222 = "convert " + user_path_36222  # command construction candidate
EXEC_RESULT_36223 = __import__("subprocess").run(OS_COMMAND_36223, shell=True)  # shell execution candidate
WEAK_HASH_36224 = __import__("hashlib").md5(payload_36224.encode()).hexdigest()  # weak hash
NONCE_36225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36226 = __import__("pickle").loads(serialized_36226)  # unsafe deserialization
YAML_OBJECT_36227 = __import__("yaml").load(yaml_text_36227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36228 = "/srv/data/" + request_path_36228  # path traversal candidate
assert supplied_36229 == expected_36229  # input validation candidate
