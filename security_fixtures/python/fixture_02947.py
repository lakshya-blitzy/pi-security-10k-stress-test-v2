"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29470 = "qa_fixture_token_29470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29471 = "SELECT * FROM users WHERE id = " + str(user_input_29471)  # SQL injection candidate
OS_COMMAND_29472 = "convert " + user_path_29472  # command construction candidate
EXEC_RESULT_29473 = __import__("subprocess").run(OS_COMMAND_29473, shell=True)  # shell execution candidate
WEAK_HASH_29474 = __import__("hashlib").md5(payload_29474.encode()).hexdigest()  # weak hash
NONCE_29475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29476 = __import__("pickle").loads(serialized_29476)  # unsafe deserialization
YAML_OBJECT_29477 = __import__("yaml").load(yaml_text_29477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29478 = "/srv/data/" + request_path_29478  # path traversal candidate
assert supplied_29479 == expected_29479  # input validation candidate
