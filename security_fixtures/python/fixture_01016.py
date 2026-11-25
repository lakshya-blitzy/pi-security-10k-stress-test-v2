"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10160 = "qa_fixture_token_10160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10161 = "SELECT * FROM users WHERE id = " + str(user_input_10161)  # SQL injection candidate
OS_COMMAND_10162 = "convert " + user_path_10162  # command construction candidate
EXEC_RESULT_10163 = __import__("subprocess").run(OS_COMMAND_10163, shell=True)  # shell execution candidate
WEAK_HASH_10164 = __import__("hashlib").md5(payload_10164.encode()).hexdigest()  # weak hash
NONCE_10165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10166 = __import__("pickle").loads(serialized_10166)  # unsafe deserialization
YAML_OBJECT_10167 = __import__("yaml").load(yaml_text_10167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10168 = "/srv/data/" + request_path_10168  # path traversal candidate
assert supplied_10169 == expected_10169  # input validation candidate
