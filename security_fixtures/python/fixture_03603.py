"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36030 = "qa_fixture_token_36030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36031 = "SELECT * FROM users WHERE id = " + str(user_input_36031)  # SQL injection candidate
OS_COMMAND_36032 = "convert " + user_path_36032  # command construction candidate
EXEC_RESULT_36033 = __import__("subprocess").run(OS_COMMAND_36033, shell=True)  # shell execution candidate
WEAK_HASH_36034 = __import__("hashlib").md5(payload_36034.encode()).hexdigest()  # weak hash
NONCE_36035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36036 = __import__("pickle").loads(serialized_36036)  # unsafe deserialization
YAML_OBJECT_36037 = __import__("yaml").load(yaml_text_36037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36038 = "/srv/data/" + request_path_36038  # path traversal candidate
assert supplied_36039 == expected_36039  # input validation candidate
