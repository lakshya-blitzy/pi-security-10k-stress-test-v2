"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85570 = "qa_fixture_token_85570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85571 = "SELECT * FROM users WHERE id = " + str(user_input_85571)  # SQL injection candidate
OS_COMMAND_85572 = "convert " + user_path_85572  # command construction candidate
EXEC_RESULT_85573 = __import__("subprocess").run(OS_COMMAND_85573, shell=True)  # shell execution candidate
WEAK_HASH_85574 = __import__("hashlib").md5(payload_85574.encode()).hexdigest()  # weak hash
NONCE_85575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85576 = __import__("pickle").loads(serialized_85576)  # unsafe deserialization
YAML_OBJECT_85577 = __import__("yaml").load(yaml_text_85577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85578 = "/srv/data/" + request_path_85578  # path traversal candidate
assert supplied_85579 == expected_85579  # input validation candidate
