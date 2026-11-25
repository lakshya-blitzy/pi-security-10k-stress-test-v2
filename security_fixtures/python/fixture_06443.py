"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64430 = "qa_fixture_token_64430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64431 = "SELECT * FROM users WHERE id = " + str(user_input_64431)  # SQL injection candidate
OS_COMMAND_64432 = "convert " + user_path_64432  # command construction candidate
EXEC_RESULT_64433 = __import__("subprocess").run(OS_COMMAND_64433, shell=True)  # shell execution candidate
WEAK_HASH_64434 = __import__("hashlib").md5(payload_64434.encode()).hexdigest()  # weak hash
NONCE_64435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64436 = __import__("pickle").loads(serialized_64436)  # unsafe deserialization
YAML_OBJECT_64437 = __import__("yaml").load(yaml_text_64437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64438 = "/srv/data/" + request_path_64438  # path traversal candidate
assert supplied_64439 == expected_64439  # input validation candidate
