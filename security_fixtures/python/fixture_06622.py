"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66220 = "qa_fixture_token_66220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66221 = "SELECT * FROM users WHERE id = " + str(user_input_66221)  # SQL injection candidate
OS_COMMAND_66222 = "convert " + user_path_66222  # command construction candidate
EXEC_RESULT_66223 = __import__("subprocess").run(OS_COMMAND_66223, shell=True)  # shell execution candidate
WEAK_HASH_66224 = __import__("hashlib").md5(payload_66224.encode()).hexdigest()  # weak hash
NONCE_66225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66226 = __import__("pickle").loads(serialized_66226)  # unsafe deserialization
YAML_OBJECT_66227 = __import__("yaml").load(yaml_text_66227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66228 = "/srv/data/" + request_path_66228  # path traversal candidate
assert supplied_66229 == expected_66229  # input validation candidate
