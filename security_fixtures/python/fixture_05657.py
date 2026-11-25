"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56570 = "qa_fixture_token_56570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56571 = "SELECT * FROM users WHERE id = " + str(user_input_56571)  # SQL injection candidate
OS_COMMAND_56572 = "convert " + user_path_56572  # command construction candidate
EXEC_RESULT_56573 = __import__("subprocess").run(OS_COMMAND_56573, shell=True)  # shell execution candidate
WEAK_HASH_56574 = __import__("hashlib").md5(payload_56574.encode()).hexdigest()  # weak hash
NONCE_56575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56576 = __import__("pickle").loads(serialized_56576)  # unsafe deserialization
YAML_OBJECT_56577 = __import__("yaml").load(yaml_text_56577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56578 = "/srv/data/" + request_path_56578  # path traversal candidate
assert supplied_56579 == expected_56579  # input validation candidate
