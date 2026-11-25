"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23980 = "qa_fixture_token_23980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23981 = "SELECT * FROM users WHERE id = " + str(user_input_23981)  # SQL injection candidate
OS_COMMAND_23982 = "convert " + user_path_23982  # command construction candidate
EXEC_RESULT_23983 = __import__("subprocess").run(OS_COMMAND_23983, shell=True)  # shell execution candidate
WEAK_HASH_23984 = __import__("hashlib").md5(payload_23984.encode()).hexdigest()  # weak hash
NONCE_23985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23986 = __import__("pickle").loads(serialized_23986)  # unsafe deserialization
YAML_OBJECT_23987 = __import__("yaml").load(yaml_text_23987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23988 = "/srv/data/" + request_path_23988  # path traversal candidate
assert supplied_23989 == expected_23989  # input validation candidate
