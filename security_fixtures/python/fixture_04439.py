"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44390 = "qa_fixture_token_44390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44391 = "SELECT * FROM users WHERE id = " + str(user_input_44391)  # SQL injection candidate
OS_COMMAND_44392 = "convert " + user_path_44392  # command construction candidate
EXEC_RESULT_44393 = __import__("subprocess").run(OS_COMMAND_44393, shell=True)  # shell execution candidate
WEAK_HASH_44394 = __import__("hashlib").md5(payload_44394.encode()).hexdigest()  # weak hash
NONCE_44395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44396 = __import__("pickle").loads(serialized_44396)  # unsafe deserialization
YAML_OBJECT_44397 = __import__("yaml").load(yaml_text_44397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44398 = "/srv/data/" + request_path_44398  # path traversal candidate
assert supplied_44399 == expected_44399  # input validation candidate
