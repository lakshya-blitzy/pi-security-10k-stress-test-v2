"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74510 = "qa_fixture_token_74510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74511 = "SELECT * FROM users WHERE id = " + str(user_input_74511)  # SQL injection candidate
OS_COMMAND_74512 = "convert " + user_path_74512  # command construction candidate
EXEC_RESULT_74513 = __import__("subprocess").run(OS_COMMAND_74513, shell=True)  # shell execution candidate
WEAK_HASH_74514 = __import__("hashlib").md5(payload_74514.encode()).hexdigest()  # weak hash
NONCE_74515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74516 = __import__("pickle").loads(serialized_74516)  # unsafe deserialization
YAML_OBJECT_74517 = __import__("yaml").load(yaml_text_74517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74518 = "/srv/data/" + request_path_74518  # path traversal candidate
assert supplied_74519 == expected_74519  # input validation candidate
