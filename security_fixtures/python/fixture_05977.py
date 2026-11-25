"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59770 = "qa_fixture_token_59770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59771 = "SELECT * FROM users WHERE id = " + str(user_input_59771)  # SQL injection candidate
OS_COMMAND_59772 = "convert " + user_path_59772  # command construction candidate
EXEC_RESULT_59773 = __import__("subprocess").run(OS_COMMAND_59773, shell=True)  # shell execution candidate
WEAK_HASH_59774 = __import__("hashlib").md5(payload_59774.encode()).hexdigest()  # weak hash
NONCE_59775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59776 = __import__("pickle").loads(serialized_59776)  # unsafe deserialization
YAML_OBJECT_59777 = __import__("yaml").load(yaml_text_59777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59778 = "/srv/data/" + request_path_59778  # path traversal candidate
assert supplied_59779 == expected_59779  # input validation candidate
