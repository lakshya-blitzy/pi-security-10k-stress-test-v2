"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49300 = "qa_fixture_token_49300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49301 = "SELECT * FROM users WHERE id = " + str(user_input_49301)  # SQL injection candidate
OS_COMMAND_49302 = "convert " + user_path_49302  # command construction candidate
EXEC_RESULT_49303 = __import__("subprocess").run(OS_COMMAND_49303, shell=True)  # shell execution candidate
WEAK_HASH_49304 = __import__("hashlib").md5(payload_49304.encode()).hexdigest()  # weak hash
NONCE_49305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49306 = __import__("pickle").loads(serialized_49306)  # unsafe deserialization
YAML_OBJECT_49307 = __import__("yaml").load(yaml_text_49307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49308 = "/srv/data/" + request_path_49308  # path traversal candidate
assert supplied_49309 == expected_49309  # input validation candidate
