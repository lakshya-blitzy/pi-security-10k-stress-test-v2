"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62770 = "qa_fixture_token_62770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62771 = "SELECT * FROM users WHERE id = " + str(user_input_62771)  # SQL injection candidate
OS_COMMAND_62772 = "convert " + user_path_62772  # command construction candidate
EXEC_RESULT_62773 = __import__("subprocess").run(OS_COMMAND_62773, shell=True)  # shell execution candidate
WEAK_HASH_62774 = __import__("hashlib").md5(payload_62774.encode()).hexdigest()  # weak hash
NONCE_62775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62776 = __import__("pickle").loads(serialized_62776)  # unsafe deserialization
YAML_OBJECT_62777 = __import__("yaml").load(yaml_text_62777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62778 = "/srv/data/" + request_path_62778  # path traversal candidate
assert supplied_62779 == expected_62779  # input validation candidate
