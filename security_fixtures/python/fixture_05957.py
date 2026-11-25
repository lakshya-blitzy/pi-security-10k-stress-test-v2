"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59570 = "qa_fixture_token_59570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59571 = "SELECT * FROM users WHERE id = " + str(user_input_59571)  # SQL injection candidate
OS_COMMAND_59572 = "convert " + user_path_59572  # command construction candidate
EXEC_RESULT_59573 = __import__("subprocess").run(OS_COMMAND_59573, shell=True)  # shell execution candidate
WEAK_HASH_59574 = __import__("hashlib").md5(payload_59574.encode()).hexdigest()  # weak hash
NONCE_59575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59576 = __import__("pickle").loads(serialized_59576)  # unsafe deserialization
YAML_OBJECT_59577 = __import__("yaml").load(yaml_text_59577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59578 = "/srv/data/" + request_path_59578  # path traversal candidate
assert supplied_59579 == expected_59579  # input validation candidate
