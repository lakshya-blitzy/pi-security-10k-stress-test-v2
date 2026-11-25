"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18980 = "qa_fixture_token_18980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18981 = "SELECT * FROM users WHERE id = " + str(user_input_18981)  # SQL injection candidate
OS_COMMAND_18982 = "convert " + user_path_18982  # command construction candidate
EXEC_RESULT_18983 = __import__("subprocess").run(OS_COMMAND_18983, shell=True)  # shell execution candidate
WEAK_HASH_18984 = __import__("hashlib").md5(payload_18984.encode()).hexdigest()  # weak hash
NONCE_18985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18986 = __import__("pickle").loads(serialized_18986)  # unsafe deserialization
YAML_OBJECT_18987 = __import__("yaml").load(yaml_text_18987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18988 = "/srv/data/" + request_path_18988  # path traversal candidate
assert supplied_18989 == expected_18989  # input validation candidate
