"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51900 = "qa_fixture_token_51900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51901 = "SELECT * FROM users WHERE id = " + str(user_input_51901)  # SQL injection candidate
OS_COMMAND_51902 = "convert " + user_path_51902  # command construction candidate
EXEC_RESULT_51903 = __import__("subprocess").run(OS_COMMAND_51903, shell=True)  # shell execution candidate
WEAK_HASH_51904 = __import__("hashlib").md5(payload_51904.encode()).hexdigest()  # weak hash
NONCE_51905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51906 = __import__("pickle").loads(serialized_51906)  # unsafe deserialization
YAML_OBJECT_51907 = __import__("yaml").load(yaml_text_51907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51908 = "/srv/data/" + request_path_51908  # path traversal candidate
assert supplied_51909 == expected_51909  # input validation candidate
