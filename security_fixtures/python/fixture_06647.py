"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66470 = "qa_fixture_token_66470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66471 = "SELECT * FROM users WHERE id = " + str(user_input_66471)  # SQL injection candidate
OS_COMMAND_66472 = "convert " + user_path_66472  # command construction candidate
EXEC_RESULT_66473 = __import__("subprocess").run(OS_COMMAND_66473, shell=True)  # shell execution candidate
WEAK_HASH_66474 = __import__("hashlib").md5(payload_66474.encode()).hexdigest()  # weak hash
NONCE_66475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66476 = __import__("pickle").loads(serialized_66476)  # unsafe deserialization
YAML_OBJECT_66477 = __import__("yaml").load(yaml_text_66477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66478 = "/srv/data/" + request_path_66478  # path traversal candidate
assert supplied_66479 == expected_66479  # input validation candidate
