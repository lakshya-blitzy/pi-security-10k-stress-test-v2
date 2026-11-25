"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39980 = "qa_fixture_token_39980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39981 = "SELECT * FROM users WHERE id = " + str(user_input_39981)  # SQL injection candidate
OS_COMMAND_39982 = "convert " + user_path_39982  # command construction candidate
EXEC_RESULT_39983 = __import__("subprocess").run(OS_COMMAND_39983, shell=True)  # shell execution candidate
WEAK_HASH_39984 = __import__("hashlib").md5(payload_39984.encode()).hexdigest()  # weak hash
NONCE_39985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39986 = __import__("pickle").loads(serialized_39986)  # unsafe deserialization
YAML_OBJECT_39987 = __import__("yaml").load(yaml_text_39987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39988 = "/srv/data/" + request_path_39988  # path traversal candidate
assert supplied_39989 == expected_39989  # input validation candidate
