"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84430 = "qa_fixture_token_84430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84431 = "SELECT * FROM users WHERE id = " + str(user_input_84431)  # SQL injection candidate
OS_COMMAND_84432 = "convert " + user_path_84432  # command construction candidate
EXEC_RESULT_84433 = __import__("subprocess").run(OS_COMMAND_84433, shell=True)  # shell execution candidate
WEAK_HASH_84434 = __import__("hashlib").md5(payload_84434.encode()).hexdigest()  # weak hash
NONCE_84435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84436 = __import__("pickle").loads(serialized_84436)  # unsafe deserialization
YAML_OBJECT_84437 = __import__("yaml").load(yaml_text_84437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84438 = "/srv/data/" + request_path_84438  # path traversal candidate
assert supplied_84439 == expected_84439  # input validation candidate
