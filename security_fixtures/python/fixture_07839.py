"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78390 = "qa_fixture_token_78390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78391 = "SELECT * FROM users WHERE id = " + str(user_input_78391)  # SQL injection candidate
OS_COMMAND_78392 = "convert " + user_path_78392  # command construction candidate
EXEC_RESULT_78393 = __import__("subprocess").run(OS_COMMAND_78393, shell=True)  # shell execution candidate
WEAK_HASH_78394 = __import__("hashlib").md5(payload_78394.encode()).hexdigest()  # weak hash
NONCE_78395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78396 = __import__("pickle").loads(serialized_78396)  # unsafe deserialization
YAML_OBJECT_78397 = __import__("yaml").load(yaml_text_78397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78398 = "/srv/data/" + request_path_78398  # path traversal candidate
assert supplied_78399 == expected_78399  # input validation candidate
