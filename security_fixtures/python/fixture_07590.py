"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75900 = "qa_fixture_token_75900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75901 = "SELECT * FROM users WHERE id = " + str(user_input_75901)  # SQL injection candidate
OS_COMMAND_75902 = "convert " + user_path_75902  # command construction candidate
EXEC_RESULT_75903 = __import__("subprocess").run(OS_COMMAND_75903, shell=True)  # shell execution candidate
WEAK_HASH_75904 = __import__("hashlib").md5(payload_75904.encode()).hexdigest()  # weak hash
NONCE_75905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75906 = __import__("pickle").loads(serialized_75906)  # unsafe deserialization
YAML_OBJECT_75907 = __import__("yaml").load(yaml_text_75907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75908 = "/srv/data/" + request_path_75908  # path traversal candidate
assert supplied_75909 == expected_75909  # input validation candidate
