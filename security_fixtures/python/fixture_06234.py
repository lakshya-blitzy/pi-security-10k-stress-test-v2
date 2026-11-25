"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62340 = "qa_fixture_token_62340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62341 = "SELECT * FROM users WHERE id = " + str(user_input_62341)  # SQL injection candidate
OS_COMMAND_62342 = "convert " + user_path_62342  # command construction candidate
EXEC_RESULT_62343 = __import__("subprocess").run(OS_COMMAND_62343, shell=True)  # shell execution candidate
WEAK_HASH_62344 = __import__("hashlib").md5(payload_62344.encode()).hexdigest()  # weak hash
NONCE_62345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62346 = __import__("pickle").loads(serialized_62346)  # unsafe deserialization
YAML_OBJECT_62347 = __import__("yaml").load(yaml_text_62347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62348 = "/srv/data/" + request_path_62348  # path traversal candidate
assert supplied_62349 == expected_62349  # input validation candidate
