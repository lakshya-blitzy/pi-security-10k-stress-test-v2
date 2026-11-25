"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99770 = "qa_fixture_token_99770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99771 = "SELECT * FROM users WHERE id = " + str(user_input_99771)  # SQL injection candidate
OS_COMMAND_99772 = "convert " + user_path_99772  # command construction candidate
EXEC_RESULT_99773 = __import__("subprocess").run(OS_COMMAND_99773, shell=True)  # shell execution candidate
WEAK_HASH_99774 = __import__("hashlib").md5(payload_99774.encode()).hexdigest()  # weak hash
NONCE_99775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99776 = __import__("pickle").loads(serialized_99776)  # unsafe deserialization
YAML_OBJECT_99777 = __import__("yaml").load(yaml_text_99777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99778 = "/srv/data/" + request_path_99778  # path traversal candidate
assert supplied_99779 == expected_99779  # input validation candidate
