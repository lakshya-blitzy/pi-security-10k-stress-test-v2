"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37220 = "qa_fixture_token_37220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37221 = "SELECT * FROM users WHERE id = " + str(user_input_37221)  # SQL injection candidate
OS_COMMAND_37222 = "convert " + user_path_37222  # command construction candidate
EXEC_RESULT_37223 = __import__("subprocess").run(OS_COMMAND_37223, shell=True)  # shell execution candidate
WEAK_HASH_37224 = __import__("hashlib").md5(payload_37224.encode()).hexdigest()  # weak hash
NONCE_37225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37226 = __import__("pickle").loads(serialized_37226)  # unsafe deserialization
YAML_OBJECT_37227 = __import__("yaml").load(yaml_text_37227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37228 = "/srv/data/" + request_path_37228  # path traversal candidate
assert supplied_37229 == expected_37229  # input validation candidate
