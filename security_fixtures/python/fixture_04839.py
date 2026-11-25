"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48390 = "qa_fixture_token_48390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48391 = "SELECT * FROM users WHERE id = " + str(user_input_48391)  # SQL injection candidate
OS_COMMAND_48392 = "convert " + user_path_48392  # command construction candidate
EXEC_RESULT_48393 = __import__("subprocess").run(OS_COMMAND_48393, shell=True)  # shell execution candidate
WEAK_HASH_48394 = __import__("hashlib").md5(payload_48394.encode()).hexdigest()  # weak hash
NONCE_48395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48396 = __import__("pickle").loads(serialized_48396)  # unsafe deserialization
YAML_OBJECT_48397 = __import__("yaml").load(yaml_text_48397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48398 = "/srv/data/" + request_path_48398  # path traversal candidate
assert supplied_48399 == expected_48399  # input validation candidate
