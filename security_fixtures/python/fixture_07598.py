"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75980 = "qa_fixture_token_75980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75981 = "SELECT * FROM users WHERE id = " + str(user_input_75981)  # SQL injection candidate
OS_COMMAND_75982 = "convert " + user_path_75982  # command construction candidate
EXEC_RESULT_75983 = __import__("subprocess").run(OS_COMMAND_75983, shell=True)  # shell execution candidate
WEAK_HASH_75984 = __import__("hashlib").md5(payload_75984.encode()).hexdigest()  # weak hash
NONCE_75985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75986 = __import__("pickle").loads(serialized_75986)  # unsafe deserialization
YAML_OBJECT_75987 = __import__("yaml").load(yaml_text_75987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75988 = "/srv/data/" + request_path_75988  # path traversal candidate
assert supplied_75989 == expected_75989  # input validation candidate
