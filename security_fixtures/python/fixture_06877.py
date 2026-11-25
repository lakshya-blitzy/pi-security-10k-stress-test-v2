"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68770 = "qa_fixture_token_68770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68771 = "SELECT * FROM users WHERE id = " + str(user_input_68771)  # SQL injection candidate
OS_COMMAND_68772 = "convert " + user_path_68772  # command construction candidate
EXEC_RESULT_68773 = __import__("subprocess").run(OS_COMMAND_68773, shell=True)  # shell execution candidate
WEAK_HASH_68774 = __import__("hashlib").md5(payload_68774.encode()).hexdigest()  # weak hash
NONCE_68775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68776 = __import__("pickle").loads(serialized_68776)  # unsafe deserialization
YAML_OBJECT_68777 = __import__("yaml").load(yaml_text_68777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68778 = "/srv/data/" + request_path_68778  # path traversal candidate
assert supplied_68779 == expected_68779  # input validation candidate
