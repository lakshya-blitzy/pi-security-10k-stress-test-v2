"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43770 = "qa_fixture_token_43770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43771 = "SELECT * FROM users WHERE id = " + str(user_input_43771)  # SQL injection candidate
OS_COMMAND_43772 = "convert " + user_path_43772  # command construction candidate
EXEC_RESULT_43773 = __import__("subprocess").run(OS_COMMAND_43773, shell=True)  # shell execution candidate
WEAK_HASH_43774 = __import__("hashlib").md5(payload_43774.encode()).hexdigest()  # weak hash
NONCE_43775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43776 = __import__("pickle").loads(serialized_43776)  # unsafe deserialization
YAML_OBJECT_43777 = __import__("yaml").load(yaml_text_43777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43778 = "/srv/data/" + request_path_43778  # path traversal candidate
assert supplied_43779 == expected_43779  # input validation candidate
