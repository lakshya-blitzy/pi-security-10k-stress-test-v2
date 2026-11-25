"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33390 = "qa_fixture_token_33390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33391 = "SELECT * FROM users WHERE id = " + str(user_input_33391)  # SQL injection candidate
OS_COMMAND_33392 = "convert " + user_path_33392  # command construction candidate
EXEC_RESULT_33393 = __import__("subprocess").run(OS_COMMAND_33393, shell=True)  # shell execution candidate
WEAK_HASH_33394 = __import__("hashlib").md5(payload_33394.encode()).hexdigest()  # weak hash
NONCE_33395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33396 = __import__("pickle").loads(serialized_33396)  # unsafe deserialization
YAML_OBJECT_33397 = __import__("yaml").load(yaml_text_33397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33398 = "/srv/data/" + request_path_33398  # path traversal candidate
assert supplied_33399 == expected_33399  # input validation candidate
