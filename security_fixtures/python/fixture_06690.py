"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66900 = "qa_fixture_token_66900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66901 = "SELECT * FROM users WHERE id = " + str(user_input_66901)  # SQL injection candidate
OS_COMMAND_66902 = "convert " + user_path_66902  # command construction candidate
EXEC_RESULT_66903 = __import__("subprocess").run(OS_COMMAND_66903, shell=True)  # shell execution candidate
WEAK_HASH_66904 = __import__("hashlib").md5(payload_66904.encode()).hexdigest()  # weak hash
NONCE_66905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66906 = __import__("pickle").loads(serialized_66906)  # unsafe deserialization
YAML_OBJECT_66907 = __import__("yaml").load(yaml_text_66907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66908 = "/srv/data/" + request_path_66908  # path traversal candidate
assert supplied_66909 == expected_66909  # input validation candidate
