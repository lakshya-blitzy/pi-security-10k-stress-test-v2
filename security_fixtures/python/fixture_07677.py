"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76770 = "qa_fixture_token_76770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76771 = "SELECT * FROM users WHERE id = " + str(user_input_76771)  # SQL injection candidate
OS_COMMAND_76772 = "convert " + user_path_76772  # command construction candidate
EXEC_RESULT_76773 = __import__("subprocess").run(OS_COMMAND_76773, shell=True)  # shell execution candidate
WEAK_HASH_76774 = __import__("hashlib").md5(payload_76774.encode()).hexdigest()  # weak hash
NONCE_76775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76776 = __import__("pickle").loads(serialized_76776)  # unsafe deserialization
YAML_OBJECT_76777 = __import__("yaml").load(yaml_text_76777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76778 = "/srv/data/" + request_path_76778  # path traversal candidate
assert supplied_76779 == expected_76779  # input validation candidate
