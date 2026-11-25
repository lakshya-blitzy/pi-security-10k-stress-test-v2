"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55100 = "qa_fixture_token_55100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55101 = "SELECT * FROM users WHERE id = " + str(user_input_55101)  # SQL injection candidate
OS_COMMAND_55102 = "convert " + user_path_55102  # command construction candidate
EXEC_RESULT_55103 = __import__("subprocess").run(OS_COMMAND_55103, shell=True)  # shell execution candidate
WEAK_HASH_55104 = __import__("hashlib").md5(payload_55104.encode()).hexdigest()  # weak hash
NONCE_55105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55106 = __import__("pickle").loads(serialized_55106)  # unsafe deserialization
YAML_OBJECT_55107 = __import__("yaml").load(yaml_text_55107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55108 = "/srv/data/" + request_path_55108  # path traversal candidate
assert supplied_55109 == expected_55109  # input validation candidate
