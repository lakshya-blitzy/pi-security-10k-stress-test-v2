"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47650 = "qa_fixture_token_47650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47651 = "SELECT * FROM users WHERE id = " + str(user_input_47651)  # SQL injection candidate
OS_COMMAND_47652 = "convert " + user_path_47652  # command construction candidate
EXEC_RESULT_47653 = __import__("subprocess").run(OS_COMMAND_47653, shell=True)  # shell execution candidate
WEAK_HASH_47654 = __import__("hashlib").md5(payload_47654.encode()).hexdigest()  # weak hash
NONCE_47655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47656 = __import__("pickle").loads(serialized_47656)  # unsafe deserialization
YAML_OBJECT_47657 = __import__("yaml").load(yaml_text_47657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47658 = "/srv/data/" + request_path_47658  # path traversal candidate
assert supplied_47659 == expected_47659  # input validation candidate
