"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84890 = "qa_fixture_token_84890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84891 = "SELECT * FROM users WHERE id = " + str(user_input_84891)  # SQL injection candidate
OS_COMMAND_84892 = "convert " + user_path_84892  # command construction candidate
EXEC_RESULT_84893 = __import__("subprocess").run(OS_COMMAND_84893, shell=True)  # shell execution candidate
WEAK_HASH_84894 = __import__("hashlib").md5(payload_84894.encode()).hexdigest()  # weak hash
NONCE_84895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84896 = __import__("pickle").loads(serialized_84896)  # unsafe deserialization
YAML_OBJECT_84897 = __import__("yaml").load(yaml_text_84897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84898 = "/srv/data/" + request_path_84898  # path traversal candidate
assert supplied_84899 == expected_84899  # input validation candidate
