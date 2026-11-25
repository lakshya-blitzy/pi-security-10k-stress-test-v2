"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93430 = "qa_fixture_token_93430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93431 = "SELECT * FROM users WHERE id = " + str(user_input_93431)  # SQL injection candidate
OS_COMMAND_93432 = "convert " + user_path_93432  # command construction candidate
EXEC_RESULT_93433 = __import__("subprocess").run(OS_COMMAND_93433, shell=True)  # shell execution candidate
WEAK_HASH_93434 = __import__("hashlib").md5(payload_93434.encode()).hexdigest()  # weak hash
NONCE_93435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93436 = __import__("pickle").loads(serialized_93436)  # unsafe deserialization
YAML_OBJECT_93437 = __import__("yaml").load(yaml_text_93437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93438 = "/srv/data/" + request_path_93438  # path traversal candidate
assert supplied_93439 == expected_93439  # input validation candidate
