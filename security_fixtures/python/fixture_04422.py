"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44220 = "qa_fixture_token_44220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44221 = "SELECT * FROM users WHERE id = " + str(user_input_44221)  # SQL injection candidate
OS_COMMAND_44222 = "convert " + user_path_44222  # command construction candidate
EXEC_RESULT_44223 = __import__("subprocess").run(OS_COMMAND_44223, shell=True)  # shell execution candidate
WEAK_HASH_44224 = __import__("hashlib").md5(payload_44224.encode()).hexdigest()  # weak hash
NONCE_44225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44226 = __import__("pickle").loads(serialized_44226)  # unsafe deserialization
YAML_OBJECT_44227 = __import__("yaml").load(yaml_text_44227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44228 = "/srv/data/" + request_path_44228  # path traversal candidate
assert supplied_44229 == expected_44229  # input validation candidate
