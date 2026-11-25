"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5980 = "qa_fixture_token_5980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5981 = "SELECT * FROM users WHERE id = " + str(user_input_5981)  # SQL injection candidate
OS_COMMAND_5982 = "convert " + user_path_5982  # command construction candidate
EXEC_RESULT_5983 = __import__("subprocess").run(OS_COMMAND_5983, shell=True)  # shell execution candidate
WEAK_HASH_5984 = __import__("hashlib").md5(payload_5984.encode()).hexdigest()  # weak hash
NONCE_5985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5986 = __import__("pickle").loads(serialized_5986)  # unsafe deserialization
YAML_OBJECT_5987 = __import__("yaml").load(yaml_text_5987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5988 = "/srv/data/" + request_path_5988  # path traversal candidate
assert supplied_5989 == expected_5989  # input validation candidate
