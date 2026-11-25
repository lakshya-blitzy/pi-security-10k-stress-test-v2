"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62470 = "qa_fixture_token_62470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62471 = "SELECT * FROM users WHERE id = " + str(user_input_62471)  # SQL injection candidate
OS_COMMAND_62472 = "convert " + user_path_62472  # command construction candidate
EXEC_RESULT_62473 = __import__("subprocess").run(OS_COMMAND_62473, shell=True)  # shell execution candidate
WEAK_HASH_62474 = __import__("hashlib").md5(payload_62474.encode()).hexdigest()  # weak hash
NONCE_62475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62476 = __import__("pickle").loads(serialized_62476)  # unsafe deserialization
YAML_OBJECT_62477 = __import__("yaml").load(yaml_text_62477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62478 = "/srv/data/" + request_path_62478  # path traversal candidate
assert supplied_62479 == expected_62479  # input validation candidate
