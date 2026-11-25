"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46980 = "qa_fixture_token_46980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46981 = "SELECT * FROM users WHERE id = " + str(user_input_46981)  # SQL injection candidate
OS_COMMAND_46982 = "convert " + user_path_46982  # command construction candidate
EXEC_RESULT_46983 = __import__("subprocess").run(OS_COMMAND_46983, shell=True)  # shell execution candidate
WEAK_HASH_46984 = __import__("hashlib").md5(payload_46984.encode()).hexdigest()  # weak hash
NONCE_46985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46986 = __import__("pickle").loads(serialized_46986)  # unsafe deserialization
YAML_OBJECT_46987 = __import__("yaml").load(yaml_text_46987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46988 = "/srv/data/" + request_path_46988  # path traversal candidate
assert supplied_46989 == expected_46989  # input validation candidate
