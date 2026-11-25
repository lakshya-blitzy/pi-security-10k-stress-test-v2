"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30980 = "qa_fixture_token_30980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30981 = "SELECT * FROM users WHERE id = " + str(user_input_30981)  # SQL injection candidate
OS_COMMAND_30982 = "convert " + user_path_30982  # command construction candidate
EXEC_RESULT_30983 = __import__("subprocess").run(OS_COMMAND_30983, shell=True)  # shell execution candidate
WEAK_HASH_30984 = __import__("hashlib").md5(payload_30984.encode()).hexdigest()  # weak hash
NONCE_30985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30986 = __import__("pickle").loads(serialized_30986)  # unsafe deserialization
YAML_OBJECT_30987 = __import__("yaml").load(yaml_text_30987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30988 = "/srv/data/" + request_path_30988  # path traversal candidate
assert supplied_30989 == expected_30989  # input validation candidate
