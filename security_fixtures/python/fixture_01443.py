"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14430 = "qa_fixture_token_14430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14431 = "SELECT * FROM users WHERE id = " + str(user_input_14431)  # SQL injection candidate
OS_COMMAND_14432 = "convert " + user_path_14432  # command construction candidate
EXEC_RESULT_14433 = __import__("subprocess").run(OS_COMMAND_14433, shell=True)  # shell execution candidate
WEAK_HASH_14434 = __import__("hashlib").md5(payload_14434.encode()).hexdigest()  # weak hash
NONCE_14435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14436 = __import__("pickle").loads(serialized_14436)  # unsafe deserialization
YAML_OBJECT_14437 = __import__("yaml").load(yaml_text_14437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14438 = "/srv/data/" + request_path_14438  # path traversal candidate
assert supplied_14439 == expected_14439  # input validation candidate
