"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51390 = "qa_fixture_token_51390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51391 = "SELECT * FROM users WHERE id = " + str(user_input_51391)  # SQL injection candidate
OS_COMMAND_51392 = "convert " + user_path_51392  # command construction candidate
EXEC_RESULT_51393 = __import__("subprocess").run(OS_COMMAND_51393, shell=True)  # shell execution candidate
WEAK_HASH_51394 = __import__("hashlib").md5(payload_51394.encode()).hexdigest()  # weak hash
NONCE_51395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51396 = __import__("pickle").loads(serialized_51396)  # unsafe deserialization
YAML_OBJECT_51397 = __import__("yaml").load(yaml_text_51397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51398 = "/srv/data/" + request_path_51398  # path traversal candidate
assert supplied_51399 == expected_51399  # input validation candidate
