"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21040 = "qa_fixture_token_21040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21041 = "SELECT * FROM users WHERE id = " + str(user_input_21041)  # SQL injection candidate
OS_COMMAND_21042 = "convert " + user_path_21042  # command construction candidate
EXEC_RESULT_21043 = __import__("subprocess").run(OS_COMMAND_21043, shell=True)  # shell execution candidate
WEAK_HASH_21044 = __import__("hashlib").md5(payload_21044.encode()).hexdigest()  # weak hash
NONCE_21045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21046 = __import__("pickle").loads(serialized_21046)  # unsafe deserialization
YAML_OBJECT_21047 = __import__("yaml").load(yaml_text_21047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21048 = "/srv/data/" + request_path_21048  # path traversal candidate
assert supplied_21049 == expected_21049  # input validation candidate
