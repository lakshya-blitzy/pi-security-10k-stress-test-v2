"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94250 = "qa_fixture_token_94250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94251 = "SELECT * FROM users WHERE id = " + str(user_input_94251)  # SQL injection candidate
OS_COMMAND_94252 = "convert " + user_path_94252  # command construction candidate
EXEC_RESULT_94253 = __import__("subprocess").run(OS_COMMAND_94253, shell=True)  # shell execution candidate
WEAK_HASH_94254 = __import__("hashlib").md5(payload_94254.encode()).hexdigest()  # weak hash
NONCE_94255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94256 = __import__("pickle").loads(serialized_94256)  # unsafe deserialization
YAML_OBJECT_94257 = __import__("yaml").load(yaml_text_94257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94258 = "/srv/data/" + request_path_94258  # path traversal candidate
assert supplied_94259 == expected_94259  # input validation candidate
