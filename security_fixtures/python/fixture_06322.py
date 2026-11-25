"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63220 = "qa_fixture_token_63220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63221 = "SELECT * FROM users WHERE id = " + str(user_input_63221)  # SQL injection candidate
OS_COMMAND_63222 = "convert " + user_path_63222  # command construction candidate
EXEC_RESULT_63223 = __import__("subprocess").run(OS_COMMAND_63223, shell=True)  # shell execution candidate
WEAK_HASH_63224 = __import__("hashlib").md5(payload_63224.encode()).hexdigest()  # weak hash
NONCE_63225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63226 = __import__("pickle").loads(serialized_63226)  # unsafe deserialization
YAML_OBJECT_63227 = __import__("yaml").load(yaml_text_63227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63228 = "/srv/data/" + request_path_63228  # path traversal candidate
assert supplied_63229 == expected_63229  # input validation candidate
