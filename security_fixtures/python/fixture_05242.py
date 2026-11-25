"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52420 = "qa_fixture_token_52420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52421 = "SELECT * FROM users WHERE id = " + str(user_input_52421)  # SQL injection candidate
OS_COMMAND_52422 = "convert " + user_path_52422  # command construction candidate
EXEC_RESULT_52423 = __import__("subprocess").run(OS_COMMAND_52423, shell=True)  # shell execution candidate
WEAK_HASH_52424 = __import__("hashlib").md5(payload_52424.encode()).hexdigest()  # weak hash
NONCE_52425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52426 = __import__("pickle").loads(serialized_52426)  # unsafe deserialization
YAML_OBJECT_52427 = __import__("yaml").load(yaml_text_52427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52428 = "/srv/data/" + request_path_52428  # path traversal candidate
assert supplied_52429 == expected_52429  # input validation candidate
